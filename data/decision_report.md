# Decision Report

- generated_at: 2026-07-28T04:21:18.706616+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9676**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9676, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_BB3S | 6/20 | 30.0% | +2.48% | **+0.74%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.05% | **+1.07%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.77% | **+0.73%** |
| MARKET_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 148件 (TP 51 / SL 92 / EXP 5)
- 最新: BANK/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.92
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$469.10** / 初期 $100.00 (+369.10%)
- 確定: 3446件 (Win 1090 / Loss 1119 / Flat 1237) / skip 2791件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.37% 残高後 $469.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1862件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0373 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.30** / 初期 $100.00 (+8.30%)
- 確定: 696件 (Win 225 / Loss 265 / Flat 206) / pending 2件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $108.30

## 6. Latest Market Context

- 更新: 2026-07-28T04:21:11.800917+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63326.2
- Funnel: target 902 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +72.36% | $11,785,565.05 |
| ON/USDT:USDT | +23.27% | $13,776,956.44 |
| RIF/USDT:USDT | +17.99% | $7,444,822.15 |
| SOONNETWORK/USDT:USDT | +15.61% | $1,460,571.70 |
| BULLA/USDT:USDT | +13.55% | $1,036,165.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +4.53% | +4.50% |
| ON/USDT:USDT | below_1h_threshold | +3.27% | +3.25% |
| BULLA/USDT:USDT | below_1h_threshold | +2.84% | +2.82% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +2.43% | +2.41% |
| O/USDT:USDT | below_1h_threshold | +1.44% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
