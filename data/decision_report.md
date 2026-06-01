# Decision Report

- generated_at: 2026-06-01T20:21:06.472214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5364**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5364, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.53% | **+0.77%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.45% | **+1.16%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.18% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 1031件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T20:21:03.737415+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=71585.1
- Funnel: target 773 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +33.09% | $5,337,305.79 |
| SLX/USDT:USDT | +16.34% | $11,577,037.63 |
| PORTAL/USDT:USDT | +15.87% | $43,867,986.62 |
| PLAY/USDT:USDT | +14.84% | $7,597,133.21 |
| VIC/USDT:USDT | +13.02% | $2,094,490.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VIC/USDT:USDT | below_1h_threshold | +3.62% | +3.60% |
| BILL/USDT:USDT | below_1h_threshold | +2.54% | +2.52% |
| W/USDT:USDT | below_1h_threshold | +2.30% | +2.28% |
| VVV/USDT:USDT | below_1h_threshold | +2.19% | +2.17% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.10% | +2.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
