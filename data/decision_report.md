# Decision Report

- generated_at: 2026-06-02T04:18:25.377968+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5402**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=5402, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.83% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.90% | **+0.49%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.62% | **+0.37%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.12% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.43** / 初期 $100.00 (+33.43%)
- 確定: 914件 (Win 213 / Loss 272 / Flat 429) / skip 1049件
- 成長率目線: 平均log +0.000316 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $133.43

## 4. Latest Market Context

- 更新: 2026-06-02T04:18:22.301095+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=70787.6
- Funnel: target 777 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +25.96% | $4,591,617.47 |
| LAB/USDT:USDT | +21.80% | $200,286,733.22 |
| ESPORTS/USDT:USDT | +20.71% | $10,967,599.18 |
| MRVLSTOCK/USDT:USDT | +20.15% | $1,539,111.03 |
| WLD/USDT:USDT | +17.39% | $140,423,844.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +3.08% | +3.26% |
| H/USDT:USDT | below_1h_threshold | +2.80% | +2.98% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.63% | +2.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.35% | +1.54% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.33% | +1.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
