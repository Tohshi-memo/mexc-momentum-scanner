# Decision Report

- generated_at: 2026-08-05T06:11:15.123381+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10372**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10372, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +3.56% | **+3.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.06% | **+1.85%** |
| MARKET_LONG | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.93% | **+1.25%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.78% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$623.79** / 初期 $100.00 (+523.79%)
- 確定: 3763件 (Win 1195 / Loss 1230 / Flat 1338) / skip 3170件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $623.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$145.56** / 初期 $100.00 (+45.56%)
- 確定: 1306件 (Win 369 / Loss 303 / Flat 634) / skip 2477件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1353 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $145.56

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.42** / 初期 $100.00 (+19.42%)
- 確定: 1121件 (Win 361 / Loss 430 / Flat 330) / pending 4件 / skip 720件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000479 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.42

## 6. Latest Market Context

- 更新: 2026-08-05T06:11:07.622510+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64300.8
- Funnel: target 939 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +87.01% | $12,216,320.82 |
| HFT/USDT:USDT | +56.04% | $1,545,023.56 |
| BLESS/USDT:USDT | +48.09% | $24,455,442.89 |
| BICO/USDT:USDT | +46.64% | $16,128,498.03 |
| MARSCOIN/USDT:USDT | +33.41% | $1,182,279.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.16% | +3.17% |
| BEAT/USDT:USDT | below_1h_threshold | +2.71% | +2.72% |
| MUU/USDT:USDT | below_1h_threshold | +2.50% | +2.51% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.22% | +2.23% |
| SOXL/USDT:USDT | below_1h_threshold | +2.03% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
