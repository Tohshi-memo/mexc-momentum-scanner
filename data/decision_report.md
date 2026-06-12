# Decision Report

- generated_at: 2026-06-12T13:53:55.998960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6514**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6514, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.33% | **+0.81%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.71% | **+0.46%** |
| LIMIT_BB3S | 4/16 | 25.0% | +1.30% | **+0.33%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.91% | **+1.43%** |
| ASK_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.97% | **+0.39%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.69% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$95.64** / 初期 $100.00 (-4.36%)
- 確定トレード: 19件 (TP 3 / SL 15 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.64
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.19** / 初期 $100.00 (+67.19%)
- 確定: 1387件 (Win 382 / Loss 449 / Flat 556) / skip 1688件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $167.19

## 4. Latest Market Context

- 更新: 2026-06-12T13:53:52.930776+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=63226.7
- Funnel: target 774 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +114.08% | $51,477,792.84 |
| VELVET/USDT:USDT | +89.31% | $161,210,844.02 |
| NAORIS/USDT:USDT | +47.13% | $6,240,306.37 |
| AIN/USDT:USDT | +42.88% | $1,323,091.57 |
| SKYAI/USDT:USDT | +40.09% | $18,255,566.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.75% | +5.07% |
| H/USDT:USDT | below_1h_threshold | +4.38% | +4.71% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.27% | +4.60% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.17% | +4.49% |
| STG/USDT:USDT | below_1h_threshold | +3.73% | +4.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
