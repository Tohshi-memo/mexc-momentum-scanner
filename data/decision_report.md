# Decision Report

- generated_at: 2026-05-11T02:17:42.341592+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4003**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=4003, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +2.96% | **+1.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.31% | **+1.18%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.35% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.35% | **+1.64%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.37% | **+1.17%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.27% | **+1.08%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.35% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.66** / 初期 $100.00 (+9.66%)
- 確定: 209件 (Win 53 / Loss 71 / Flat 85) / skip 355件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $109.66

## 4. Latest Market Context

- 更新: 2026-05-11T02:17:39.180136+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=81234.8
- Funnel: target 775 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +32.47% | $9,628,506.55 |
| ALCH/USDT:USDT | +21.41% | $3,879,310.96 |
| TROLLSOL/USDT:USDT | +15.40% | $5,359,897.55 |
| B/USDT:USDT | +12.50% | $2,705,023.64 |
| OPG/USDT:USDT | +12.21% | $1,123,945.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPG/USDT:USDT | below_1h_threshold | +2.17% | +2.45% |
| JASMY/USDT:USDT | below_1h_threshold | +1.10% | +1.38% |
| TRUTH/USDT:USDT | below_1h_threshold | +0.88% | +1.16% |
| ORCA/USDT:USDT | below_1h_threshold | +0.83% | +1.11% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.32% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
