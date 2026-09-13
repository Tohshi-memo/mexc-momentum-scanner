# Decision Report

- generated_at: 2026-09-13T19:06:14.105905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14463**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14463, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.96% | **+0.89%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.90% | **+2.34%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.47% | **+1.79%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.14% | **+0.69%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.56% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,075.03** / 初期 $100.00 (+975.03%)
- 確定: 5433件 (Win 1635 / Loss 1761 / Flat 2037) / skip 5591件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,075.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.25** / 初期 $100.00 (+131.25%)
- 確定: 2981件 (Win 829 / Loss 710 / Flat 1442) / skip 4893件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1221 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $231.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.72** / 初期 $100.00 (+26.72%)
- 確定: 2856件 (Win 850 / Loss 1105 / Flat 901) / pending 0件 / skip 3077件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000388 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.72

## 6. Latest Market Context

- 更新: 2026-09-13T19:06:03.720859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77346.7
- Funnel: target 1068 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POWER/USDT:USDT | +10.74% | $1,074,744.50 |
| PONS/USDT:USDT | +10.15% | $4,837,597.08 |
| NIULAI/USDT:USDT | +7.05% | $5,174,340.72 |
| BTW/USDT:USDT | +6.06% | $7,689,229.75 |
| USELESS/USDT:USDT | +5.84% | $4,635,227.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EGLD/USDT:USDT | below_1h_threshold | +1.34% | +1.29% |
| UAI/USDT:USDT | below_1h_threshold | +0.80% | +0.75% |
| FILECOIN/USDT:USDT | below_1h_threshold | +0.70% | +0.66% |
| OPENAI/USDT:USDT | below_1h_threshold | +0.33% | +0.28% |
| VET/USDT:USDT | below_1h_threshold | +0.32% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
