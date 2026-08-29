# Decision Report

- generated_at: 2026-08-29T16:51:18.659900+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12953**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12953, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.95% | **+1.38%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.38% | **+0.83%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.70% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$737.28** / 初期 $100.00 (+637.28%)
- 確定: 4723件 (Win 1432 / Loss 1550 / Flat 1741) / skip 4791件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $737.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$160.74** / 初期 $100.00 (+60.74%)
- 確定: 2037件 (Win 557 / Loss 488 / Flat 992) / skip 4327件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0819 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $160.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2387件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-29T16:51:09.133329+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=78005.3
- Funnel: target 1023 → liquid 137 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +24.01% | $5,308,977.40 |
| FONE/USDT:USDT | +5.23% | $1,282,160.93 |
| DOS/USDT:USDT | +4.76% | $2,119,217.25 |
| UNI/USDT:USDT | +3.01% | $7,850,896.27 |
| VELVET/USDT:USDT | +2.68% | $1,504,560.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOS/USDT:USDT | below_1h_threshold | +4.77% | +4.53% |
| UNI/USDT:USDT | below_1h_threshold | +3.01% | +2.78% |
| LIGHT/USDT:USDT | below_1h_threshold | +2.71% | +2.47% |
| VELVET/USDT:USDT | below_1h_threshold | +2.69% | +2.45% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.53% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
