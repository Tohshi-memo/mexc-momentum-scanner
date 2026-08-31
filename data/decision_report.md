# Decision Report

- generated_at: 2026-08-31T02:31:17.816923+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13123**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13123, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/20 | 40.0% | +3.24% | **+1.30%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.46% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.82% | **+0.91%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$793.56** / 初期 $100.00 (+693.56%)
- 確定: 4855件 (Win 1478 / Loss 1599 / Flat 1778) / skip 4829件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZORA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $793.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.14** / 初期 $100.00 (+73.14%)
- 確定: 2167件 (Win 601 / Loss 528 / Flat 1038) / skip 4367件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0533 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $173.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2083件 (Win 610 / Loss 812 / Flat 661) / pending 0件 / skip 2509件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-31T02:31:07.651997+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=77849.5
- Funnel: target 1026 → liquid 140 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1, 4h RSI 95.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKR/USDT:USDT | +98.69% | $25,972,016.54 |
| HEMI/USDT:USDT | +43.09% | $3,463,467.15 |
| BASECAT/USDT:USDT | +36.18% | $1,475,326.61 |
| ZORA/USDT:USDT | +29.09% | $2,628,859.86 |
| CYS/USDT:USDT | +5.75% | $4,175,161.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +2.82% | +2.51% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.23% | +1.92% |
| AKE/USDT:USDT | below_1h_threshold | +2.07% | +1.76% |
| HEMI/USDT:USDT | below_1h_threshold | +2.04% | +1.73% |
| TUT/USDT:USDT | below_1h_threshold | +1.90% | +1.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
