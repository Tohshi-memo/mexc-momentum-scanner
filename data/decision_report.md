# Decision Report

- generated_at: 2026-07-04T08:52:13.799252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8237**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8237, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.29% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$314.31** / 初期 $100.00 (+214.31%)
- 確定: 2554件 (Win 799 / Loss 851 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARPA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $314.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.26** / 初期 $100.00 (+7.26%)
- 確定: 633件 (Win 152 / Loss 153 / Flat 328) / skip 1015件
- 成長率目線: 平均log +0.000111 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0651 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARPA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.26

## 5. Latest Market Context

- 更新: 2026-07-04T08:52:05.422174+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=62617.1
- Funnel: target 834 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +80.35% | $5,153,552.89 |
| TLM/USDT:USDT | +52.73% | $43,915,544.84 |
| LAB/USDT:USDT | +48.15% | $56,155,855.41 |
| HMSTR/USDT:USDT | +48.05% | $5,512,245.40 |
| BAS/USDT:USDT | +40.83% | $4,406,926.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.23% | +4.12% |
| BAS/USDT:USDT | below_1h_threshold | +2.60% | +2.50% |
| NEX/USDT:USDT | below_1h_threshold | +1.94% | +1.83% |
| TAIKO/USDT:USDT | below_1h_threshold | +1.47% | +1.36% |
| CRO/USDT:USDT | below_1h_threshold | +1.24% | +1.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
