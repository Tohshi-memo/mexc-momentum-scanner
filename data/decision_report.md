# Decision Report

- generated_at: 2026-06-10T16:46:55.237695+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6233**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6233, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.16% | **+2.21%** |
| ASK_LONG | 20/20 | 100.0% | +1.67% | **+1.67%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.56% | **+1.28%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.00** / 初期 $100.00 (+49.00%)
- 確定: 1229件 (Win 306 / Loss 384 / Flat 539) / skip 1565件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.00

## 4. Latest Market Context

- 更新: 2026-06-10T16:46:48.615094+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.80% price=62099.8
- Funnel: target 785 → liquid 155 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.5 >= 65=1, 4h RSI 82.8 >= 65=1, 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +9.63% | $14,274,308.55 |
| FOLKS/USDT:USDT | +8.62% | $3,170,852.82 |
| OPN/USDT:USDT | +6.46% | $4,478,692.57 |
| BEAT/USDT:USDT | +6.14% | $113,144,671.92 |
| HMSTR/USDT:USDT | +3.94% | $2,699,305.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +3.92% | +4.72% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.91% | +4.71% |
| BTW/USDT:USDT | below_1h_threshold | +2.76% | +3.57% |
| BLESS/USDT:USDT | below_1h_threshold | +2.68% | +3.49% |
| SIREN/USDT:USDT | below_1h_threshold | +2.43% | +3.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
