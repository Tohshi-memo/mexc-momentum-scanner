# Decision Report

- generated_at: 2026-10-23T22:16:15.066711+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17290**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17290, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-3.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.40% | **-3.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 10/20 | 50.0% | +1.75% | **+0.87%** |
| LIMIT_9PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_8PCT | 13/20 | 65.0% | +0.28% | **+0.19%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.08% | **+0.16%** |
| LIMIT_6PCT | 16/20 | 80.0% | +0.10% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.00% | **-0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.16% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7298件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6772件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1414 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5451件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000405 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T22:16:05.785559+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81311.3
- Funnel: target 1088 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +40.16% | $9,346,532.24 |
| IRYS/USDT:USDT | +39.19% | $91,918,780.38 |
| AKE/USDT:USDT | +12.06% | $18,477,780.75 |
| KIMCHI/USDT:USDT | +6.80% | $1,270,261.33 |
| SOXS/USDT:USDT | +3.05% | $31,656,018.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.08% | +4.13% |
| KIMCHI/USDT:USDT | below_1h_threshold | +1.14% | +1.18% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.61% | +0.65% |
| BTW/USDT:USDT | below_1h_threshold | +0.49% | +0.53% |
| S/USDT:USDT | below_1h_threshold | +0.49% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
