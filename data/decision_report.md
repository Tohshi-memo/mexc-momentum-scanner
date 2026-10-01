# Decision Report

- generated_at: 2026-10-01T14:56:45.516385+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15912**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15912, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.34% | **-1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.27% | **+0.49%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.33% | **+0.46%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.31% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.75% | **+1.67%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.77% | **+1.24%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.52% | **+1.09%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,307.49** / 初期 $100.00 (+1207.49%)
- 確定: 6025件 (Win 1785 / Loss 1938 / Flat 2302) / skip 6448件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,307.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.08** / 初期 $100.00 (+178.08%)
- 確定: 3565件 (Win 992 / Loss 820 / Flat 1753) / skip 5758件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1411 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $278.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4075件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000402 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T14:56:28.998396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=83890.0
- Funnel: target 1097 → liquid 177 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +78.32% | $7,478,405.04 |
| MOVR/USDT:USDT | +49.70% | $21,247,610.24 |
| CAP/USDT:USDT | +29.10% | $1,132,614.90 |
| CT/USDT:USDT | +20.90% | $7,285,088.74 |
| ACNSTOCK/USDT:USDT | +18.69% | $2,329,303.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACNSTOCK/USDT:USDT | below_1h_threshold | +3.79% | +3.81% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.24% |
| STX/USDT:USDT | below_1h_threshold | +2.19% | +2.21% |
| TWSTSTOCK/USDT:USDT | below_1h_threshold | +1.47% | +1.50% |
| SYN/USDT:USDT | below_1h_threshold | +1.40% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
