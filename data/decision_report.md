# Decision Report

- generated_at: 2026-10-15T15:52:09.192109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16753**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16753, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.84% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.32% | **+1.62%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.46% | **+0.74%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.24% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 240件 (TP 89 / SL 144 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,260.96** / 初期 $100.00 (+1160.96%)
- 確定: 6312件 (Win 1849 / Loss 2026 / Flat 2437) / skip 7002件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PYTH/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,260.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.10** / 初期 $100.00 (+174.10%)
- 確定: 3673件 (Win 1023 / Loss 871 / Flat 1779) / skip 6491件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4923件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-15T15:51:44.378286+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.62% price=82355.5
- Funnel: target 1090 → liquid 184 → pre 50 → checked 50 → surge 8 → strict 5
- Surge前reject: below_1h_threshold=42, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.7 >= 65=1, 4h RSI 69.7 >= 65=1, 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUFFER/USDT:USDT | +88.02% | $2,294,253.94 |
| ZEREBRO/USDT:USDT | +52.56% | $9,421,682.97 |
| ARCSOL/USDT:USDT | +33.89% | $2,793,269.77 |
| PYTH/USDT:USDT | +24.35% | $13,612,978.30 |
| STRK/USDT:USDT | +20.26% | $38,465,323.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARCSOL/USDT:USDT | below_1h_threshold | +4.96% | +4.34% |
| INJ/USDT:USDT | below_1h_threshold | +4.41% | +3.79% |
| BSPSTOCK/USDT:USDT | below_1h_threshold | +4.21% | +3.58% |
| ETHFI/USDT:USDT | below_1h_threshold | +4.01% | +3.39% |
| TIA/USDT:USDT | below_1h_threshold | +3.99% | +3.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
