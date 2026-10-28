# Decision Report

- generated_at: 2026-10-28T03:56:43.099731+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17680**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17680, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.67% | **+1.28%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.59% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,532.91** / 初期 $100.00 (+1432.91%)
- 確定: 6760件 (Win 1968 / Loss 2170 / Flat 2622) / skip 7481件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,532.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$358.49** / 初期 $100.00 (+258.49%)
- 確定: 4209件 (Win 1147 / Loss 966 / Flat 2096) / skip 6882件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0875 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $358.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5845件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T03:56:22.518739+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=81084.2
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 72.9 >= 65=1, 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +58.75% | $1,331,683.26 |
| BULLA/USDT:USDT | +50.46% | $10,671,243.65 |
| EVAA/USDT:USDT | +39.10% | $5,380,247.87 |
| APR/USDT:USDT | +18.77% | $6,533,906.44 |
| PONS/USDT:USDT | +18.24% | $2,414,162.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +3.57% | +3.36% |
| PONS/USDT:USDT | below_1h_threshold | +2.52% | +2.32% |
| USELESS/USDT:USDT | below_1h_threshold | +1.54% | +1.34% |
| ZRO/USDT:USDT | below_1h_threshold | +1.36% | +1.15% |
| PEPE/USDT:USDT | below_1h_threshold | +1.31% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
