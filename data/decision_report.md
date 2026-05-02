# Decision Report

- generated_at: 2026-05-02T05:52:10.252751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2868**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2868, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/19 | 31.6% | +3.28% | **+1.04%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.56% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T05:52:07.776007+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78148.8
- Funnel: target 755 → liquid 170 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.9 >= 65=1, 4h RSI 72.2 >= 65=1, 4h RSI 68.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +202.72% | $52,950,629.37 |
| PLAY/USDT:USDT | +19.03% | $4,662,309.35 |
| SKYAI/USDT:USDT | +11.60% | $21,612,458.95 |
| B/USDT:USDT | +11.36% | $76,827,695.66 |
| IRYS/USDT:USDT | +10.05% | $1,010,519.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.40% | +2.38% |
| LYN/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |
| COAI/USDT:USDT | below_1h_threshold | +1.72% | +1.71% |
| CHIP/USDT:USDT | below_1h_threshold | +1.70% | +1.69% |
| ORDI/USDT:USDT | below_1h_threshold | +1.64% | +1.63% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
