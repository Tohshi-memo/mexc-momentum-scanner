# Decision Report

- generated_at: 2026-09-19T20:11:27.547030+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15093**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15093, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/14 | 42.9% | +1.82% | **+0.78%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.65% | **+0.49%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.32% | **+0.46%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.08% | **+0.07%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.75% | **+1.05%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.89% | **+1.04%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | -0.01% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6014件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.08** / 初期 $100.00 (+143.08%)
- 確定: 3207件 (Win 888 / Loss 761 / Flat 1558) / skip 5297件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0339 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $243.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2974件 (Win 880 / Loss 1176 / Flat 918) / pending 0件 / skip 3592件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000406 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T20:11:14.619987+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=81386.8
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OFC/USDT:USDT | +33.05% | $1,517,222.94 |
| ONE/USDT:USDT | +30.16% | $33,138,311.55 |
| BANK/USDT:USDT | +13.78% | $1,676,705.75 |
| PEPE/USDT:USDT | +10.11% | $163,992,289.26 |
| ZIL/USDT:USDT | +7.25% | $1,148,346.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +1.48% | +1.41% |
| ZIL/USDT:USDT | below_1h_threshold | +1.00% | +0.94% |
| KORU/USDT:USDT | below_1h_threshold | +0.76% | +0.69% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.70% | +0.64% |
| ALGO/USDT:USDT | below_1h_threshold | +0.58% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
