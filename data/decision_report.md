# Decision Report

- generated_at: 2026-06-12T05:13:27.812647+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6462**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6462, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.15% | **+0.64%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.10% | **+0.61%** |
| LIMIT_BB3S | 2/18 | 11.1% | +2.90% | **+0.32%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.27% | **+0.22%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.64% | **+1.85%** |
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.32% | **+1.13%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$156.78** / 初期 $100.00 (+56.78%)
- 確定: 1337件 (Win 352 / Loss 429 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000336 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $156.78

## 4. Latest Market Context

- 更新: 2026-06-12T05:13:19.664599+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=63410.4
- Funnel: target 783 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +74.52% | $139,941,425.22 |
| H/USDT:USDT | +32.44% | $39,638,041.58 |
| ESPORTS/USDT:USDT | +31.34% | $30,836,364.09 |
| XPL/USDT:USDT | +31.13% | $6,274,279.89 |
| NAORIS/USDT:USDT | +26.16% | $1,736,396.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.28% | +3.69% |
| LAB/USDT:USDT | below_1h_threshold | +3.27% | +3.68% |
| STG/USDT:USDT | below_1h_threshold | +2.79% | +3.20% |
| BSB/USDT:USDT | below_1h_threshold | +1.46% | +1.87% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.43% | +1.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
