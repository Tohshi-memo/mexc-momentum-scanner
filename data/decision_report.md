# Decision Report

- generated_at: 2026-05-06T16:24:55.899096+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3481**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3481, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.49% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.57% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.13% | **+1.25%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.74% | **+1.09%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 33件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T16:24:50.155559+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81561.7
- Funnel: target 770 → liquid 192 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1, 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +8.28% | $8,696,275.21 |
| LAB/USDT:USDT | +7.13% | $195,167,090.08 |
| FHE/USDT:USDT | +5.10% | $33,921,551.34 |
| B3/USDT:USDT | +4.40% | $6,165,106.43 |
| IO/USDT:USDT | +3.15% | $15,930,717.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B3/USDT:USDT | below_1h_threshold | +4.41% | +4.52% |
| IO/USDT:USDT | below_1h_threshold | +3.15% | +3.27% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.36% | +2.48% |
| AR/USDT:USDT | below_1h_threshold | +2.11% | +2.22% |
| LYN/USDT:USDT | below_1h_threshold | +1.84% | +1.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
