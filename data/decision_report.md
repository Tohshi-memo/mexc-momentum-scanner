# Decision Report

- generated_at: 2026-10-01T14:01:36.512912+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15906**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15906, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.10% | **+0.09%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +0.85% | **+0.09%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +2.37% | **+1.78%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.94% | **+1.75%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.09% | **+1.15%** |
| MARKET_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.34% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,299.12** / 初期 $100.00 (+1199.12%)
- 確定: 6021件 (Win 1783 / Loss 1936 / Flat 2302) / skip 6446件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.67% 残高後 $1,299.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.55** / 初期 $100.00 (+174.55%)
- 確定: 3559件 (Win 988 / Loss 818 / Flat 1753) / skip 5758件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1193 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.45% 残高後 $274.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4067件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000319 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T14:01:25.144886+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=83760.8
- Funnel: target 1097 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +78.45% | $6,463,941.83 |
| MOVR/USDT:USDT | +53.81% | $20,113,195.23 |
| CT/USDT:USDT | +26.65% | $6,955,829.26 |
| ACNSTOCK/USDT:USDT | +22.63% | $2,280,649.42 |
| MONAD/USDT:USDT | +16.25% | $10,229,810.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACNSTOCK/USDT:USDT | below_1h_threshold | +3.79% | +3.97% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.39% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.46% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.37% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.78% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
