# Decision Report

- generated_at: 2026-10-14T20:51:20.217597+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16702, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.77% | **-0.35%** |
| LIMIT_10PCT | 2/20 | 10.0% | -4.00% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +3.14% | **+3.14%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.20% | **+1.87%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.52% | **+1.64%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.58% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 239件 (TP 89 / SL 143 / EXP 7)
- 最新: ARCSOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,286.66** / 初期 $100.00 (+1186.66%)
- 確定: 6298件 (Win 1846 / Loss 2018 / Flat 2434) / skip 6965件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARCSOL/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.61% 残高後 $1,286.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.60** / 初期 $100.00 (+175.60%)
- 確定: 3665件 (Win 1021 / Loss 867 / Flat 1777) / skip 6448件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0975 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AVA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $275.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4862件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000248 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-14T20:51:08.448889+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=81626.7
- Funnel: target 1085 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +20.30% | $1,385,087.81 |
| NIL/USDT:USDT | +18.87% | $6,534,697.41 |
| WAL/USDT:USDT | +15.12% | $11,176,207.35 |
| ARCSOL/USDT:USDT | +12.82% | $1,833,504.69 |
| 1000RATS/USDT:USDT | +7.55% | $3,092,843.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PYTH/USDT:USDT | below_1h_threshold | +3.62% | +3.83% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.76% | +1.97% |
| QNT/USDT:USDT | below_1h_threshold | +1.71% | +1.92% |
| W/USDT:USDT | below_1h_threshold | +1.54% | +1.75% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +1.38% | +1.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
