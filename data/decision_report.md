# Decision Report

- generated_at: 2026-05-06T14:52:46.376110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3471**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3471, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.85% | **+1.16%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.62% | **+0.81%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.79% | **+2.79%** |
| MARKET_LONG | 20/20 | 100.0% | +2.77% | **+2.77%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.74% | **+1.64%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.94% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 23件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T14:52:43.281742+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=81573.4
- Funnel: target 770 → liquid 205 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1, 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +106.49% | $3,872,666.70 |
| LAB/USDT:USDT | +46.02% | $165,327,107.57 |
| ZEC/USDT:USDT | +33.57% | $774,076,241.29 |
| IO/USDT:USDT | +32.14% | $15,323,862.64 |
| BILL/USDT:USDT | +32.04% | $5,929,953.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +4.94% | +5.00% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.30% | +4.36% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +3.73% | +3.79% |
| TAG/USDT:USDT | below_1h_threshold | +3.54% | +3.60% |
| M/USDT:USDT | below_1h_threshold | +2.59% | +2.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
