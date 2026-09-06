# Decision Report

- generated_at: 2026-09-06T04:16:06.337485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13794**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13794, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.88% | **+0.18%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.01% | **+0.01%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.05% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.03% | **+1.52%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +4.36% | **+1.45%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.28% | **+1.37%** |
| MARKET_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$867.25** / 初期 $100.00 (+767.25%)
- 確定: 5100件 (Win 1532 / Loss 1664 / Flat 1904) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAY/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $867.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.15** / 初期 $100.00 (+91.15%)
- 確定: 2539件 (Win 709 / Loss 601 / Flat 1229) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0486 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $191.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.29** / 初期 $100.00 (+20.29%)
- 確定: 2410件 (Win 719 / Loss 914 / Flat 777) / pending 3件 / skip 2854件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAY/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $120.29

## 6. Latest Market Context

- 更新: 2026-09-06T04:15:59.728670+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=79950.0
- Funnel: target 1050 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +44.69% | $123,256,481.57 |
| RAY/USDT:USDT | +40.99% | $1,519,812.07 |
| UAI/USDT:USDT | +23.34% | $9,959,399.03 |
| FLOCK/USDT:USDT | +22.32% | $1,091,761.35 |
| BASECAT/USDT:USDT | +17.55% | $2,119,495.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +1.74% | +1.79% |
| CHIP/USDT:USDT | below_1h_threshold | +1.21% | +1.26% |
| LIT/USDT:USDT | below_1h_threshold | +0.72% | +0.77% |
| ZRO/USDT:USDT | below_1h_threshold | +0.22% | +0.28% |
| ZEC/USDT:USDT | below_1h_threshold | +0.16% | +0.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
