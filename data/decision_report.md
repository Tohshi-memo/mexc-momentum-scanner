# Decision Report

- generated_at: 2026-06-02T23:27:03.175737+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5500**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=5500, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.67% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.38% | **+0.38%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.41% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.41% | **+0.63%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1084件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T23:27:00.161077+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=66246.0
- Funnel: target 770 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +32.85% | $12,809,219.56 |
| US/USDT:USDT | +28.17% | $7,392,269.91 |
| ESPORTS/USDT:USDT | +17.02% | $8,258,141.72 |
| LIT/USDT:USDT | +15.41% | $6,711,490.17 |
| BBSTOCK/USDT:USDT | +14.28% | $1,768,855.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.88% | +2.05% |
| US/USDT:USDT | below_1h_threshold | +1.77% | +1.94% |
| USOIL/USDT:USDT | below_1h_threshold | +1.66% | +1.82% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.38% | +1.54% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.24% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
