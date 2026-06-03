# Decision Report

- generated_at: 2026-06-03T19:04:06.889784+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5572**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=5572, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +5.00% | **+2.22%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.96% | **+0.79%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.68% | **+0.61%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.75% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1129件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T19:04:04.495545+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=66007.4
- Funnel: target 768 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +50.94% | $10,723,528.60 |
| STO/USDT:USDT | +38.70% | $1,801,346.60 |
| BP/USDT:USDT | +10.26% | $1,440,631.06 |
| MAGMA/USDT:USDT | +9.27% | $3,656,334.28 |
| LAB/USDT:USDT | +8.02% | $262,349,445.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STO/USDT:USDT | below_1h_threshold | +3.37% | +3.36% |
| EPIC/USDT:USDT | below_1h_threshold | +1.95% | +1.94% |
| BEAT/USDT:USDT | below_1h_threshold | +1.52% | +1.52% |
| XPL/USDT:USDT | below_1h_threshold | +1.20% | +1.20% |
| ZRO/USDT:USDT | below_1h_threshold | +0.80% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
