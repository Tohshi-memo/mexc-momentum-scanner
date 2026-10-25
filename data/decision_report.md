# Decision Report

- generated_at: 2026-10-25T04:06:27.954301+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17397**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17397, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.46% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.44% | **+0.65%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.40% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,451.34** / 初期 $100.00 (+1351.34%)
- 確定: 6650件 (Win 1929 / Loss 2119 / Flat 2602) / skip 7308件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,451.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$302.14** / 初期 $100.00 (+202.14%)
- 確定: 3940件 (Win 1087 / Loss 923 / Flat 1930) / skip 6868件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2014 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $302.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5556件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000620 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T04:06:15.504085+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80800.0
- Funnel: target 1079 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +42.31% | $2,720,178.21 |
| APR/USDT:USDT | +42.21% | $2,213,731.53 |
| USELESS/USDT:USDT | +21.02% | $3,822,996.59 |
| AGT/USDT:USDT | +17.12% | $5,695,150.83 |
| GRASS/USDT:USDT | +9.49% | $1,738,179.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIGHT/USDT:USDT | below_1h_threshold | +2.33% | +2.36% |
| SNXX/USDT:USDT | below_1h_threshold | +1.10% | +1.13% |
| T/USDT:USDT | below_1h_threshold | +1.02% | +1.05% |
| MUU/USDT:USDT | below_1h_threshold | +0.81% | +0.85% |
| KORU/USDT:USDT | below_1h_threshold | +0.57% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
