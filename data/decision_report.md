# Decision Report

- generated_at: 2026-06-09T17:55:24.874114+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6153**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6153, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.02% | **+0.82%** |
| ASK | 20/20 | 100.0% | +0.25% | **+0.25%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.10% | **+0.03%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.93% | **+0.49%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.28%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.43% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 12件 (TP 1 / SL 10 / EXP 1)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.01** / 初期 $100.00 (+48.01%)
- 確定: 1188件 (Win 297 / Loss 374 / Flat 517) / skip 1526件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.01

## 4. Latest Market Context

- 更新: 2026-06-09T17:55:17.427932+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.53% price=61694.6
- Funnel: target 778 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SENT/USDT:USDT | +12.65% | $1,102,287.51 |
| HOME/USDT:USDT | +10.12% | $3,763,568.80 |
| ESPORTS/USDT:USDT | +8.69% | $24,277,995.61 |
| LIT/USDT:USDT | +7.27% | $3,070,729.22 |
| BTW/USDT:USDT | +7.24% | $4,249,466.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_relative_strength | +5.03% | +4.50% |
| ZEC/USDT:USDT | below_1h_threshold | +3.54% | +3.00% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.48% | +2.95% |
| HOME/USDT:USDT | below_1h_threshold | +3.30% | +2.77% |
| PLAY/USDT:USDT | below_1h_threshold | +2.87% | +2.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
