# Decision Report

- generated_at: 2026-07-19T10:06:19.755807+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9021**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9021, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.76% | **-2.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/18 | 22.2% | +4.03% | **+0.90%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.15% | **+0.65%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.71% | **+0.61%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.75% | **+4.75%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.58% | **+2.69%** |
| MARKET_LONG | 20/20 | 100.0% | +2.56% | **+2.56%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +4.35% | **+1.52%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +2.56% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$400.31** / 初期 $100.00 (+300.31%)
- 確定: 3083件 (Win 966 / Loss 980 / Flat 1137) / skip 2499件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $400.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.29** / 初期 $100.00 (+27.29%)
- 確定: 982件 (Win 252 / Loss 200 / Flat 530) / skip 1450件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1865 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $127.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.41** / 初期 $100.00 (+0.41%)
- 確定: 223件 (Win 71 / Loss 112 / Flat 40) / pending 6件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000519 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.41

## 6. Latest Market Context

- 更新: 2026-07-19T10:06:11.821762+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64518.5
- Funnel: target 885 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +113.84% | $47,076,053.68 |
| BANK/USDT:USDT | +77.30% | $21,732,644.85 |
| TLM/USDT:USDT | +47.65% | $5,991,722.46 |
| B/USDT:USDT | +40.35% | $41,688,765.19 |
| TAG/USDT:USDT | +28.00% | $3,768,593.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +1.57% | +1.54% |
| TLM/USDT:USDT | below_1h_threshold | +1.51% | +1.47% |
| BULLA/USDT:USDT | below_1h_threshold | +0.85% | +0.82% |
| ZBT/USDT:USDT | below_1h_threshold | +0.82% | +0.79% |
| PI/USDT:USDT | below_1h_threshold | +0.74% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
