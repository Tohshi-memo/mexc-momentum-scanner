# Decision Report

- generated_at: 2026-07-19T11:16:14.612781+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9025**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9025, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.17% | **-2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_4PCT | 16/20 | 80.0% | +1.00% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.97% | **+0.66%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.97% | **+1.28%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.80% | **+0.72%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$396.32** / 初期 $100.00 (+296.32%)
- 確定: 3087件 (Win 966 / Loss 982 / Flat 1139) / skip 2499件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $396.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.40** / 初期 $100.00 (+26.40%)
- 確定: 986件 (Win 252 / Loss 202 / Flat 532) / skip 1450件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1649 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $126.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.57** / 初期 $100.00 (+0.57%)
- 確定: 227件 (Win 73 / Loss 114 / Flat 40) / pending 6件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000507 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.57

## 6. Latest Market Context

- 更新: 2026-07-19T11:16:07.978119+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64570.0
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +117.28% | $27,274,947.38 |
| ESPORTS/USDT:USDT | +82.03% | $50,380,806.75 |
| TLM/USDT:USDT | +50.83% | $6,238,619.14 |
| B/USDT:USDT | +49.11% | $40,260,089.99 |
| TAG/USDT:USDT | +28.94% | $4,369,357.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +4.01% | +4.00% |
| B/USDT:USDT | below_1h_threshold | +3.23% | +3.21% |
| KAITO/USDT:USDT | below_1h_threshold | +2.02% | +2.01% |
| TAG/USDT:USDT | below_1h_threshold | +1.40% | +1.38% |
| ZBT/USDT:USDT | below_1h_threshold | +1.24% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
