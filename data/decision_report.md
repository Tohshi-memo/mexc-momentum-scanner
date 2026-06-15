# Decision Report

- generated_at: 2026-06-15T08:15:40.840834+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6763**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6763, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.90% | **+0.27%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.17% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.00% | **-0.00%** |
| ASK | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.53% | **+1.52%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.58% | **+1.34%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.84% | **+1.34%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$177.58** / 初期 $100.00 (+77.58%)
- 確定: 1636件 (Win 428 / Loss 505 / Flat 703) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $177.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.88** / 初期 $100.00 (-1.12%)
- 確定: 130件 (Win 25 / Loss 21 / Flat 84) / skip 44件
- 成長率目線: 平均log -0.000087 / 幾何平均 -0.009% per trade / maxDD +2.07%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score -0.0053 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $98.88

## 5. Latest Market Context

- 更新: 2026-06-15T08:15:35.037619+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=65701.0
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +91.60% | $3,966,662.67 |
| EVAA/USDT:USDT | +86.25% | $24,170,794.12 |
| CLO/USDT:USDT | +42.98% | $2,157,995.95 |
| TRADOOR/USDT:USDT | +27.56% | $4,178,509.63 |
| PUFFER/USDT:USDT | +25.89% | $1,057,805.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.53% | +4.44% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.39% | +3.30% |
| CHIP/USDT:USDT | below_1h_threshold | +2.11% | +2.02% |
| AAVE/USDT:USDT | below_1h_threshold | +1.80% | +1.71% |
| H/USDT:USDT | below_1h_threshold | +1.77% | +1.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
