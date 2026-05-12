# Decision Report

- generated_at: 2026-05-12T02:58:24.060214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4091**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4091, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.26% | **+0.85%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.76% | **+0.57%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.80% | **+1.44%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.29% | **+1.22%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.07% | **+0.96%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.05% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.74** / 初期 $100.00 (+11.74%)
- 確定: 228件 (Win 60 / Loss 79 / Flat 89) / skip 424件
- 成長率目線: 平均log +0.000487 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $111.74

## 4. Latest Market Context

- 更新: 2026-05-12T02:58:17.964332+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=81204.0
- Funnel: target 762 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +53.23% | $1,984,635.72 |
| SKYAI/USDT:USDT | +35.82% | $39,934,823.43 |
| USELESS/USDT:USDT | +21.81% | $4,390,097.66 |
| SAGA/USDT:USDT | +17.42% | $7,420,153.06 |
| GUA/USDT:USDT | +16.66% | $1,110,399.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +4.59% | +4.52% |
| GUA/USDT:USDT | below_1h_threshold | +3.62% | +3.55% |
| VVV/USDT:USDT | below_1h_threshold | +3.47% | +3.40% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +2.70% | +2.63% |
| OG/USDT:USDT | below_1h_threshold | +2.20% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
