# Decision Report

- generated_at: 2026-05-06T14:27:37.814261+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3466**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3466, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +7.44% | **+1.49%** |
| LIMIT_8PCT | 5/20 | 25.0% | +4.97% | **+1.24%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.25% | **+1.09%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.99% | **+0.44%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.31% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.70% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.07% | **+0.53%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.64% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 18件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T14:27:34.558649+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81633.1
- Funnel: target 770 → liquid 203 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.9 >= 65=1, 4h RSI 76.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +86.39% | $3,447,833.31 |
| BILL/USDT:USDT | +38.70% | $5,726,885.49 |
| ZEC/USDT:USDT | +33.41% | $766,503,821.35 |
| IO/USDT:USDT | +33.24% | $15,113,101.91 |
| FHE/USDT:USDT | +30.80% | $33,578,984.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.62% | +3.60% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +2.63% | +2.62% |
| TAG/USDT:USDT | below_1h_threshold | +1.63% | +1.61% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.61% | +1.59% |
| ZEC/USDT:USDT | below_1h_threshold | +1.43% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
