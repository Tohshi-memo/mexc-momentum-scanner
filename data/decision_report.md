# Decision Report

- generated_at: 2026-07-19T10:26:18.991659+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9022**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9022, expectancy=-0.01%
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
| MARKET_LONG | 20/20 | 100.0% | +2.56% | **+2.56%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.48% | **+2.43%** |
| LIMIT_3PCT_LONG | 6/20 | 30.0% | +3.74% | **+1.12%** |
| LIMIT_2PCT_LONG | 7/20 | 35.0% | +2.05% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$400.31** / 初期 $100.00 (+300.31%)
- 確定: 3084件 (Win 966 / Loss 980 / Flat 1138) / skip 2499件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $400.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.29** / 初期 $100.00 (+27.29%)
- 確定: 983件 (Win 252 / Loss 200 / Flat 531) / skip 1450件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1780 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $127.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.58** / 初期 $100.00 (+0.58%)
- 確定: 224件 (Win 72 / Loss 112 / Flat 40) / pending 5件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000519 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.58

## 6. Latest Market Context

- 更新: 2026-07-19T10:26:11.236204+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64573.9
- Funnel: target 885 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +103.30% | $48,326,308.12 |
| BANK/USDT:USDT | +81.25% | $22,438,039.27 |
| TLM/USDT:USDT | +44.10% | $6,061,616.37 |
| B/USDT:USDT | +41.83% | $42,102,636.52 |
| TAG/USDT:USDT | +28.42% | $3,942,951.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +1.62% | +1.49% |
| BANK/USDT:USDT | below_1h_threshold | +1.55% | +1.42% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.37% | +1.25% |
| ZBT/USDT:USDT | below_1h_threshold | +1.24% | +1.11% |
| NEO/USDT:USDT | below_1h_threshold | +1.02% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
