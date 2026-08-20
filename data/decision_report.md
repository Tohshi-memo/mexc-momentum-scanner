# Decision Report

- generated_at: 2026-08-20T08:31:33.298609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=12020, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/14 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.35% | **+0.41%** |
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.48% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.21% | **+0.90%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.13% | **+0.62%** |
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.73% | **+0.37%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.24% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.20** / 初期 $100.00 (+506.20%)
- 確定: 4244件 (Win 1303 / Loss 1388 / Flat 1553) / skip 4337件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STAR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $606.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3610件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.76** / 初期 $100.00 (+16.76%)
- 確定: 1754件 (Win 520 / Loss 670 / Flat 564) / pending 3件 / skip 1737件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000489 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINIMAXSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.76

## 6. Latest Market Context

- 更新: 2026-08-20T08:31:21.858161+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.07% price=71264.3
- Funnel: target 1004 → liquid 198 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BOME/USDT:USDT | +32.02% | $4,633,462.30 |
| MAGMA/USDT:USDT | +28.83% | $7,753,186.22 |
| BASECAT/USDT:USDT | +22.62% | $1,239,714.05 |
| RED/USDT:USDT | +20.64% | $2,149,124.21 |
| RE/USDT:USDT | +19.55% | $14,669,902.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEPE/USDT:USDT | below_relative_strength | +5.54% | +3.47% |
| USELESS/USDT:USDT | below_1h_threshold | +3.56% | +1.48% |
| FLOKI/USDT:USDT | below_1h_threshold | +3.07% | +0.99% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.70% | +0.62% |
| XRP/USDT:USDT | below_1h_threshold | +2.63% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
