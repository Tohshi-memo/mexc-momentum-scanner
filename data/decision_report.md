# Decision Report

- generated_at: 2026-11-07T02:56:06.310417+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18349**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18349, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.71% | **-1.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.18% | **+0.35%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_BB3S | 2/18 | 11.1% | +0.11% | **+0.01%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.84% | **+1.53%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.97% | **+1.34%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.34% | **+1.29%** |
| LIMIT_6PCT_LONG | 4/20 | 20.0% | +5.47% | **+1.09%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.91** / 初期 $100.00 (+1385.91%)
- 確定: 7046件 (Win 2026 / Loss 2248 / Flat 2772) / skip 7864件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,485.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$390.18** / 初期 $100.00 (+290.18%)
- 確定: 4716件 (Win 1269 / Loss 1039 / Flat 2408) / skip 7044件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UVXY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $390.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6508件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T02:55:57.961387+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=75980.0
- Funnel: target 1089 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +52.53% | $59,422,904.88 |
| AIN/USDT:USDT | +28.11% | $4,831,415.74 |
| LYN/USDT:USDT | +12.27% | $1,668,310.48 |
| BTW/USDT:USDT | +11.57% | $7,185,583.68 |
| JCT/USDT:USDT | +10.67% | $5,047,584.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.72% | +3.75% |
| JCT/USDT:USDT | below_1h_threshold | +2.53% | +2.56% |
| PONS/USDT:USDT | below_1h_threshold | +1.82% | +1.84% |
| IDOL/USDT:USDT | below_1h_threshold | +1.69% | +1.71% |
| SPX/USDT:USDT | below_1h_threshold | +0.96% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
