# Decision Report

- generated_at: 2026-05-27T06:04:28.951588+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4920**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=4920, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.56% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.29% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.82% | **+0.74%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.16% | **+0.64%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.17% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.43** / 初期 $100.00 (+27.43%)
- 確定: 682件 (Win 172 / Loss 219 / Flat 291) / skip 799件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $127.43

## 4. Latest Market Context

- 更新: 2026-05-27T06:04:26.825057+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=75712.0
- Funnel: target 772 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +21.42% | $9,330,799.91 |
| REQ/USDT:USDT | +21.28% | $1,460,680.57 |
| LUNC/USDT:USDT | +12.48% | $10,827,619.50 |
| RON/USDT:USDT | +12.10% | $1,222,790.95 |
| SEI/USDT:USDT | +8.39% | $16,556,087.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +1.26% | +1.21% |
| SEI/USDT:USDT | below_1h_threshold | +1.21% | +1.16% |
| PLAY/USDT:USDT | below_1h_threshold | +0.82% | +0.77% |
| GUA/USDT:USDT | below_1h_threshold | +0.76% | +0.71% |
| REQ/USDT:USDT | below_1h_threshold | +0.47% | +0.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
