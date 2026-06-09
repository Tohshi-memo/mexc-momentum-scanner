# Decision Report

- generated_at: 2026-06-09T10:46:42.469137+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6129**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6129, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.22% | **+0.09%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.28% | **+1.48%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.03% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.68** / 初期 $100.00 (+52.68%)
- 確定: 1169件 (Win 293 / Loss 362 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000362 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $152.68

## 4. Latest Market Context

- 更新: 2026-06-09T10:46:37.267174+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62675.6
- Funnel: target 774 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +60.96% | $20,907,659.41 |
| SLX/USDT:USDT | +28.37% | $4,785,222.07 |
| POWER/USDT:USDT | +21.26% | $2,320,419.16 |
| SKHYNIXSTOCK/USDT:USDT | +9.80% | $4,310,910.26 |
| MOVE/USDT:USDT | +9.49% | $6,021,473.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +4.33% | +4.34% |
| CHIP/USDT:USDT | below_1h_threshold | +2.72% | +2.73% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.63% | +2.64% |
| INJ/USDT:USDT | below_1h_threshold | +1.57% | +1.58% |
| BANK/USDT:USDT | below_1h_threshold | +1.47% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
