# Decision Report

- generated_at: 2026-06-18T03:30:13.080631+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6998**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6998, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.45% | **+0.51%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.64% | **-0.26%** |
| LIMIT_6PCT | 6/20 | 30.0% | -1.02% | **-0.31%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.64% | **-0.33%** |
| LIMIT_8PCT | 5/20 | 25.0% | -1.60% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.69% | **+3.69%** |
| MARKET_LONG | 20/20 | 100.0% | +3.40% | **+3.40%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +3.03% | **+1.82%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.46% | **+1.73%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.75% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$216.22** / 初期 $100.00 (+116.22%)
- 確定: 1844件 (Win 513 / Loss 580 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $216.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.06** / 初期 $100.00 (+6.06%)
- 確定: 271件 (Win 75 / Loss 68 / Flat 128) / skip 138件
- 成長率目線: 平均log +0.000217 / 幾何平均 +0.022% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0950 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FOLKS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.06

## 5. Latest Market Context

- 更新: 2026-06-18T03:30:06.315254+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.56% price=64287.9
- Funnel: target 790 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.0 >= 65=1, 4h RSI 78.9 >= 65=1, 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +142.50% | $32,433,274.13 |
| O/USDT:USDT | +56.59% | $1,768,198.46 |
| SYN/USDT:USDT | +47.76% | $4,500,271.48 |
| HOME/USDT:USDT | +33.32% | $1,033,210.22 |
| H/USDT:USDT | +24.40% | $37,032,441.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.26% | +3.83% |
| EVAA/USDT:USDT | below_1h_threshold | +3.09% | +3.66% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.88% | +3.45% |
| STG/USDT:USDT | below_1h_threshold | +2.68% | +3.24% |
| ID/USDT:USDT | below_1h_threshold | +2.56% | +3.13% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
