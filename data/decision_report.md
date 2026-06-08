# Decision Report

- generated_at: 2026-06-08T07:58:28.078629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6058**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6058, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.54% | **+0.32%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.24% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.93% | **+2.36%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.15% | **+2.08%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.66% | **+1.73%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.00% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1475件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T07:58:22.492629+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=63279.8
- Funnel: target 773 → liquid 143 → pre 50 → checked 50 → surge 6 → strict 2
- Surge前reject: below_1h_threshold=43, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1, 4h RSI 81.4 >= 65=1, 4h RSI 72.9 >= 65=1, 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +51.74% | $40,940,136.42 |
| ESPORTS/USDT:USDT | +46.38% | $10,543,613.99 |
| BEAT/USDT:USDT | +45.73% | $111,152,441.86 |
| PIPPIN/USDT:USDT | +43.41% | $9,951,800.90 |
| BANK/USDT:USDT | +24.01% | $5,225,529.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_relative_strength | +5.14% | +4.63% |
| HOME/USDT:USDT | below_1h_threshold | +4.43% | +3.91% |
| VELVET/USDT:USDT | below_1h_threshold | +3.43% | +2.92% |
| VVV/USDT:USDT | below_1h_threshold | +3.43% | +2.91% |
| RAVE/USDT:USDT | below_1h_threshold | +3.42% | +2.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
