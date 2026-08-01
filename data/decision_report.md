# Decision Report

- generated_at: 2026-08-01T05:06:20.425507+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10061**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=10061, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.45% | **+0.98%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.37% | **+0.89%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.44% | **+0.30%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.19% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.51% | **-0.15%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.25% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$568.33** / 初期 $100.00 (+468.33%)
- 確定: 3613件 (Win 1153 / Loss 1183 / Flat 1277) / skip 3009件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $568.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2193件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.70** / 初期 $100.00 (+11.70%)
- 確定: 876件 (Win 283 / Loss 347 / Flat 246) / pending 4件 / skip 655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.70

## 6. Latest Market Context

- 更新: 2026-08-01T05:06:13.114718+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63075.2
- Funnel: target 921 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +31.00% | $1,238,869.32 |
| KOMA/USDT:USDT | +28.12% | $17,589,563.62 |
| BTW/USDT:USDT | +23.12% | $2,976,073.39 |
| GIGGLE/USDT:USDT | +21.89% | $24,661,862.41 |
| TLM/USDT:USDT | +13.71% | $1,892,219.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.79% | +1.79% |
| UAI/USDT:USDT | below_1h_threshold | +1.43% | +1.43% |
| TAG/USDT:USDT | below_1h_threshold | +1.27% | +1.27% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.09% | +1.09% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.96% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
