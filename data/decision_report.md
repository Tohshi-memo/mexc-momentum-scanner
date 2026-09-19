# Decision Report

- generated_at: 2026-09-19T20:56:57.340958+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15098**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15098, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/17 | 47.1% | +2.71% | **+1.27%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.63% | **+0.60%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.29% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.22% | **+0.16%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.27% | **+0.82%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.29% | **+0.77%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.50% | **+0.37%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.09% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6019件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.26** / 初期 $100.00 (+143.26%)
- 確定: 3211件 (Win 889 / Loss 761 / Flat 1561) / skip 5298件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0188 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $243.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2974件 (Win 880 / Loss 1176 / Flat 918) / pending 1件 / skip 3594件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000440 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T20:56:46.303870+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=81083.7
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +39.45% | $34,857,464.01 |
| OFC/USDT:USDT | +35.88% | $1,568,534.22 |
| BANK/USDT:USDT | +16.51% | $1,793,603.54 |
| CATE/USDT:USDT | +11.43% | $1,581,340.62 |
| PEPE/USDT:USDT | +10.12% | $168,223,060.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +3.91% | +4.21% |
| CATE/USDT:USDT | below_1h_threshold | +3.53% | +3.83% |
| EVAA/USDT:USDT | below_1h_threshold | +2.45% | +2.76% |
| S/USDT:USDT | below_1h_threshold | +1.20% | +1.51% |
| AVAX/USDT:USDT | below_1h_threshold | +1.07% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
