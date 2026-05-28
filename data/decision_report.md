# Decision Report

- generated_at: 2026-05-28T22:19:30.958806+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4994**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=4994, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.05% | **+0.82%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.76% | **+0.34%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.69% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 727件 (Win 175 / Loss 222 / Flat 330) / skip 828件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-28T22:19:28.782970+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=73665.1
- Funnel: target 772 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +41.15% | $14,394,713.55 |
| DELLSTOCK/USDT:USDT | +27.81% | $6,023,492.46 |
| CLO/USDT:USDT | +22.85% | $1,182,800.88 |
| XPL/USDT:USDT | +10.55% | $4,061,785.40 |
| VVV/USDT:USDT | +9.88% | $10,162,359.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.77% |
| XLM/USDT:USDT | below_1h_threshold | +0.69% | +0.87% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +0.44% | +0.62% |
| LIT/USDT:USDT | below_1h_threshold | +0.21% | +0.39% |
| EDEN/USDT:USDT | below_1h_threshold | +0.08% | +0.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
