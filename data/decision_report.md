# Decision Report

- generated_at: 2026-05-28T18:46:13.235257+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4986**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4986, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.84% | **-0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.72% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.91% | **+1.62%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.51% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +1.39% | **+1.22%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.69% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.69** / 初期 $100.00 (+28.69%)
- 確定: 721件 (Win 174 / Loss 221 / Flat 326) / skip 826件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.69

## 4. Latest Market Context

- 更新: 2026-05-28T18:46:10.787202+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=73591.1
- Funnel: target 773 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +31.44% | $4,840,534.43 |
| XPL/USDT:USDT | +9.86% | $3,264,005.78 |
| SWARMS/USDT:USDT | +8.68% | $1,258,704.61 |
| AR/USDT:USDT | +7.91% | $1,991,681.69 |
| VVV/USDT:USDT | +7.90% | $9,845,265.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SWARMS/USDT:USDT | below_1h_threshold | +3.77% | +3.67% |
| VVV/USDT:USDT | below_1h_threshold | +3.40% | +3.30% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.29% | +3.19% |
| LIT/USDT:USDT | below_1h_threshold | +3.16% | +3.06% |
| LAB/USDT:USDT | below_1h_threshold | +3.09% | +2.99% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
