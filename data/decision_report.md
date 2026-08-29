# Decision Report

- generated_at: 2026-08-29T10:26:14.445063+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12924**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12924, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.21% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.77%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.82% | **+0.49%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.21% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$722.18** / 初期 $100.00 (+622.18%)
- 確定: 4694件 (Win 1421 / Loss 1542 / Flat 1731) / skip 4791件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $722.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.50** / 初期 $100.00 (+58.50%)
- 確定: 2009件 (Win 548 / Loss 485 / Flat 976) / skip 4326件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0394 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $158.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.30** / 初期 $100.00 (+16.30%)
- 確定: 2019件 (Win 593 / Loss 780 / Flat 646) / pending 3件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.30

## 6. Latest Market Context

- 更新: 2026-08-29T10:26:06.640123+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77643.3
- Funnel: target 1023 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1, 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +92.44% | $1,773,362.13 |
| HNT/USDT:USDT | +81.54% | $4,443,218.79 |
| 4/USDT:USDT | +41.82% | $1,531,002.22 |
| O/USDT:USDT | +19.34% | $1,256,488.17 |
| ONG/USDT:USDT | +16.76% | $4,174,533.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +3.52% | +3.48% |
| BTR/USDT:USDT | below_1h_threshold | +2.87% | +2.84% |
| GALA/USDT:USDT | below_1h_threshold | +2.24% | +2.21% |
| DASH/USDT:USDT | below_1h_threshold | +1.40% | +1.37% |
| BTW/USDT:USDT | below_1h_threshold | +1.38% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
