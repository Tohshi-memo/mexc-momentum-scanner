# Decision Report

- generated_at: 2026-06-01T13:11:16.600580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5319**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.97% / filled 20/20。**
- 全期間 MARKET基準: n=5319, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |
| ASK | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.06% | **+0.80%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.76% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.12% | **-0.12%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.39% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 986件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T13:11:14.303256+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=71971.1
- Funnel: target 776 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +109.74% | $38,769,949.55 |
| PORTAL/USDT:USDT | +107.75% | $38,159,492.64 |
| SLX/USDT:USDT | +88.66% | $8,668,744.60 |
| LAB/USDT:USDT | +70.57% | $229,340,761.76 |
| VIC/USDT:USDT | +57.74% | $1,364,970.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +2.23% | +2.54% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.90% | +1.21% |
| USOIL/USDT:USDT | below_1h_threshold | +0.68% | +0.99% |
| CTR/USDT:USDT | below_1h_threshold | +0.63% | +0.94% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.63% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
