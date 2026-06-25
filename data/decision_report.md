# Decision Report

- generated_at: 2026-06-25T13:44:28.500197+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7559**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7559, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.64% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.84% | **+2.84%** |
| MARKET_LONG | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.34% | **+1.29%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.82% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 1988件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.89** / 初期 $100.00 (+7.89%)
- 確定: 368件 (Win 102 / Loss 99 / Flat 167) / skip 602件
- 成長率目線: 平均log +0.000206 / 幾何平均 +0.021% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0760 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.89

## 5. Latest Market Context

- 更新: 2026-06-25T13:44:23.373299+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.58% price=60247.7
- Funnel: target 806 → liquid 164 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 77.4 >= 65=1, 4h RSI 80.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +43.75% | $21,401,578.49 |
| SYN/USDT:USDT | +42.85% | $26,101,032.19 |
| HEI/USDT:USDT | +36.74% | $4,130,579.97 |
| RESOLV/USDT:USDT | +27.11% | $4,528,937.50 |
| IDOL/USDT:USDT | +21.61% | $1,016,889.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RESOLV/USDT:USDT | below_1h_threshold | +3.09% | +4.68% |
| BEAT/USDT:USDT | below_1h_threshold | +1.75% | +3.33% |
| DEXE/USDT:USDT | below_1h_threshold | +1.72% | +3.30% |
| SLX/USDT:USDT | below_1h_threshold | +1.56% | +3.14% |
| AIN/USDT:USDT | below_1h_threshold | +1.52% | +3.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
