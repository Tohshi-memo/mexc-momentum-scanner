# Decision Report

- generated_at: 2026-10-23T22:41:31.429225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17292**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17292, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 9/20 | 45.0% | +2.38% | **+1.07%** |
| LIMIT_9PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_8PCT | 12/20 | 60.0% | +0.64% | **+0.39%** |
| LIMIT_6PCT | 15/20 | 75.0% | +0.38% | **+0.28%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.08% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7300件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6774件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1267 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5454件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000405 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T22:41:20.862104+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=81101.8
- Funnel: target 1088 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +41.02% | $9,654,907.10 |
| IRYS/USDT:USDT | +31.66% | $93,429,420.53 |
| AKE/USDT:USDT | +13.41% | $18,622,309.55 |
| KIMCHI/USDT:USDT | +5.70% | $1,284,140.76 |
| SOXS/USDT:USDT | +3.42% | $32,239,538.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.83% | +5.13% |
| AXIS/USDT:USDT | below_1h_threshold | +3.43% | +3.73% |
| KIMCHI/USDT:USDT | below_1h_threshold | +0.21% | +0.51% |
| SOXS/USDT:USDT | below_1h_threshold | +0.15% | +0.46% |
| NGAS/USDT:USDT | below_1h_threshold | +0.13% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
