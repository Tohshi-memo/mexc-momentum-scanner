# Decision Report

- generated_at: 2026-07-26T05:21:37.254839+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9558**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9558, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.51% | **+0.68%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.88% | **+0.45%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.70% | **+0.45%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.39% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.24% | **+0.90%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.39% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$466.41** / 初期 $100.00 (+366.41%)
- 確定: 3386件 (Win 1077 / Loss 1098 / Flat 1211) / skip 2733件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $466.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.69** / 初期 $100.00 (+39.69%)
- 確定: 1211件 (Win 337 / Loss 268 / Flat 606) / skip 1758件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $139.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.43** / 初期 $100.00 (+9.43%)
- 確定: 601件 (Win 205 / Loss 229 / Flat 167) / pending 2件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000591 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.43

## 6. Latest Market Context

- 更新: 2026-07-26T05:21:25.159012+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64479.0
- Funnel: target 898 → liquid 119 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +64.39% | $34,183,657.84 |
| DIA/USDT:USDT | +47.43% | $1,287,551.82 |
| SHIB/USDT:USDT | +17.87% | $58,342,598.60 |
| BANK/USDT:USDT | +17.85% | $94,136,149.87 |
| LIGHT/USDT:USDT | +15.10% | $1,442,298.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHIB/USDT:USDT | below_1h_threshold | +3.54% | +3.57% |
| DIA/USDT:USDT | below_1h_threshold | +3.05% | +3.07% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.29% | +2.31% |
| WIF/USDT:USDT | below_1h_threshold | +1.33% | +1.36% |
| PEPE/USDT:USDT | below_1h_threshold | +1.13% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
