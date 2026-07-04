# Decision Report

- generated_at: 2026-07-04T06:26:34.916055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8225**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8225, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.87% | **-1.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.57% | **+0.13%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.30% | **+2.30%** |
| ASK_LONG | 20/20 | 100.0% | +2.13% | **+2.13%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.11% | **+1.27%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.26% | **+0.90%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +1.74% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$311.23** / 初期 $100.00 (+211.23%)
- 確定: 2542件 (Win 792 / Loss 846 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $311.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 621件 (Win 149 / Loss 150 / Flat 322) / skip 1015件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0680 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-07-04T06:26:28.713702+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=62331.1
- Funnel: target 834 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +73.77% | $4,700,305.99 |
| TLM/USDT:USDT | +66.34% | $42,766,975.89 |
| HMSTR/USDT:USDT | +41.25% | $3,843,849.31 |
| LAB/USDT:USDT | +35.98% | $45,873,263.61 |
| BAS/USDT:USDT | +35.42% | $4,151,630.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.28% | +4.47% |
| ARPA/USDT:USDT | below_1h_threshold | +3.17% | +3.35% |
| TLM/USDT:USDT | below_1h_threshold | +2.39% | +2.57% |
| TAIKO/USDT:USDT | below_1h_threshold | +2.16% | +2.34% |
| VELVET/USDT:USDT | below_1h_threshold | +1.83% | +2.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
