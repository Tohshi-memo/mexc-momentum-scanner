# Decision Report

- generated_at: 2026-10-24T01:06:57.612229+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17314**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17314, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 10/20 | 50.0% | +2.68% | **+1.34%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.59% | **+1.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.41% | **+0.85%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.90% | **+0.59%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +1.13% | **+0.51%** |
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.35% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.53** / 初期 $100.00 (+1210.53%)
- 確定: 6568件 (Win 1904 / Loss 2098 / Flat 2566) / skip 7307件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_9PCT` EXPIRED account +0.00% 残高後 $1,310.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6796件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0778 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5474件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000178 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T01:06:42.528404+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80620.6
- Funnel: target 1088 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +92.63% | $5,650,866.80 |
| AXIS/USDT:USDT | +30.26% | $1,882,958.12 |
| IRYS/USDT:USDT | +23.47% | $96,761,276.41 |
| AGT/USDT:USDT | +19.76% | $10,766,044.75 |
| SOXS/USDT:USDT | +3.85% | $30,102,235.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARK/USDT:USDT | below_1h_threshold | +2.29% | +2.25% |
| IRYS/USDT:USDT | below_1h_threshold | +0.54% | +0.50% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.43% | +0.39% |
| WINBONDSTOCK/USDT:USDT | below_1h_threshold | +0.42% | +0.38% |
| SOXS/USDT:USDT | below_1h_threshold | +0.40% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
