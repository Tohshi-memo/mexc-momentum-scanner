# Decision Report

- generated_at: 2026-10-14T20:26:22.528446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16701**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16701, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.53% | **-0.27%** |
| LIMIT_7PCT | 5/20 | 25.0% | -1.28% | **-0.32%** |
| LIMIT_6PCT | 5/20 | 25.0% | -1.65% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +3.14% | **+3.14%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.91% | **+2.47%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.06% | **+1.84%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.28% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 239件 (TP 89 / SL 143 / EXP 7)
- 最新: ARCSOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,286.66** / 初期 $100.00 (+1186.66%)
- 確定: 6298件 (Win 1846 / Loss 2018 / Flat 2434) / skip 6964件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARCSOL/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.61% 残高後 $1,286.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.57** / 初期 $100.00 (+176.57%)
- 確定: 3664件 (Win 1021 / Loss 866 / Flat 1777) / skip 6448件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1082 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $276.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4862件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-14T20:26:12.914167+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=81917.4
- Funnel: target 1085 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +22.13% | $1,265,763.73 |
| NIL/USDT:USDT | +15.95% | $6,227,667.77 |
| ARCSOL/USDT:USDT | +15.19% | $1,818,626.40 |
| WAL/USDT:USDT | +14.98% | $11,049,204.31 |
| AVA/USDT:USDT | +12.82% | $1,773,841.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARCSOL/USDT:USDT | below_1h_threshold | +3.11% | +2.96% |
| PYTH/USDT:USDT | below_1h_threshold | +2.91% | +2.77% |
| VVV/USDT:USDT | below_1h_threshold | +2.00% | +1.86% |
| QNT/USDT:USDT | below_1h_threshold | +1.77% | +1.62% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.49% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
