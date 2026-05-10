# Decision Report

- generated_at: 2026-05-10T20:17:38.340029+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3987**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3987, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.06% | **+0.42%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 5/13 | 38.5% | +0.02% | **+0.01%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.31% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.93% | **+1.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.48% | **+1.34%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.15% | **+0.86%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.10% | **+0.66%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.65% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.26** / 初期 $100.00 (+8.26%)
- 確定: 200件 (Win 49 / Loss 67 / Flat 84) / skip 348件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TROLLSOL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $108.26

## 4. Latest Market Context

- 更新: 2026-05-10T20:17:35.416733+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.44% price=81035.8
- Funnel: target 769 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +30.81% | $1,986,342.88 |
| TROLLSOL/USDT:USDT | +23.00% | $3,993,467.44 |
| ALCH/USDT:USDT | +22.64% | $2,722,908.83 |
| B/USDT:USDT | +15.25% | $2,139,883.94 |
| SUI/USDT:USDT | +12.24% | $648,100,441.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UKOIL/USDT:USDT | below_1h_threshold | +2.28% | +2.73% |
| USOIL/USDT:USDT | below_1h_threshold | +1.97% | +2.42% |
| TRIA/USDT:USDT | below_1h_threshold | +1.67% | +2.12% |
| BEAT/USDT:USDT | below_1h_threshold | +1.56% | +2.00% |
| ALCH/USDT:USDT | below_1h_threshold | +1.35% | +1.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
