# Decision Report

- generated_at: 2026-09-24T18:46:32.051607+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15486**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=15486, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.39% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.99% | **+0.25%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.38% | **+0.17%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.16% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/10 | 70.0% | +2.20% | **+1.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.39% | **+0.23%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.58% | **+0.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.27% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5899件 (Win 1739 / Loss 1890 / Flat 2270) / skip 6148件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$254.22** / 初期 $100.00 (+154.22%)
- 確定: 3433件 (Win 948 / Loss 791 / Flat 1694) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0268 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $254.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3801件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T18:46:20.495972+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=84400.2
- Funnel: target 1069 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAI/USDT:USDT | +31.95% | $4,871,578.35 |
| LSK/USDT:USDT | +5.61% | $15,917,186.65 |
| RAY/USDT:USDT | +4.94% | $10,306,643.27 |
| LINK/USDT:USDT | +3.73% | $51,922,434.36 |
| SOXL/USDT:USDT | +3.63% | $30,300,984.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +4.12% | +3.73% |
| LINK/USDT:USDT | below_1h_threshold | +2.85% | +2.47% |
| LSK/USDT:USDT | below_1h_threshold | +2.62% | +2.23% |
| LIT/USDT:USDT | below_1h_threshold | +1.16% | +0.77% |
| XLM/USDT:USDT | below_1h_threshold | +0.96% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
