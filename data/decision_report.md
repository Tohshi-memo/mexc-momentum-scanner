# Decision Report

- generated_at: 2026-10-24T00:56:18.700884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17312**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17312, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_7PCT | 10/20 | 50.0% | +2.68% | **+1.34%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.59% | **+1.29%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.41% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +1.28% | **+0.89%** |
| LIMIT_5PCT_LONG | 15/20 | 75.0% | +0.86% | **+0.64%** |
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +1.28% | **+0.51%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +1.13% | **+0.51%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +0.80% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.53** / 初期 $100.00 (+1210.53%)
- 確定: 6566件 (Win 1904 / Loss 2098 / Flat 2564) / skip 7307件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,310.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6794件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0925 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5474件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T00:56:07.636857+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.66% price=80622.7
- Funnel: target 1088 → liquid 168 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1, 4h RSI 71.3 >= 65=1, 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +90.00% | $5,503,397.31 |
| AXIS/USDT:USDT | +32.54% | $1,862,668.74 |
| AGT/USDT:USDT | +25.86% | $10,918,888.78 |
| IRYS/USDT:USDT | +19.09% | $96,685,069.34 |
| SOXS/USDT:USDT | +4.31% | $31,910,356.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.62% | +5.28% |
| ARK/USDT:USDT | below_1h_threshold | +1.51% | +2.17% |
| BTW/USDT:USDT | below_1h_threshold | +1.43% | +2.09% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +1.54% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.74% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
